data "aws_vpc" "existing_vpc" {
  filter {
    name   = "cidr"
    values = ["172.35.0.0/20"]
  }
}

resource "aws_security_group" "ecs_cluster_sg" {
  name        = "ecs-cluster-sg"
  vpc_id      = data.aws_vpc.existing_vpc.id

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_ecs_cluster" "cluster" {
  name = "cluster"
  vpc_config {
    vpc_id = data.aws_vpc.existing_vpc.id
    security_group_ids = [aws_security_group.ecs_cluster_sg.id]
  }
}

resource "aws_ecs_service" "my_service" {
  name            = "service"
  cluster         = aws_ecs_cluster.my_cluster.id
  task_definition = aws_ecs_task_definition.my_task_definition.arn
  desired_count   = 1
  launch_type     = "FARGATE"
  network_configuration {
    subnets         = data.aws_vpc.existing_vpc.subnet_ids
    security_groups = [aws_security_group.ecs_cluster_sg.id]
  }
}

resource "aws_ecs_task_definition" "my_task_definition" {
  family                   = "tasks"
  execution_role_arn       = "arn:aws:iam::123456789012:role/ecsTaskExecutionRole"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  container_definitions    = {
    ecs-sample = {
      image     = "public.ecr.aws/aws-containers/ecsdemo:latest"
      port_mappings = [
        {
          name          = "ecs-task"
          containerPort = 80
          protocol      = "tcp"
        }
      ]
    }
  }
}