import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { MicroserviceOptions, Transport } from '@nestjs/microservices';

async function bootstrap() {
  try {
    const app = await NestFactory.createMicroservice<MicroserviceOptions>(
      AppModule,
      {
        transport: Transport.RMQ,
        options: {
          urls: process.env.RABBITMQ_URI?.split(','),
          queue: process.env.RABBITMQ_USERS_QUEUE,
          queueOptions: {
            durable: true,
          },
        },
      },
    );

    await app.listen();
    console.log(
      `Users microservice is listening to RabbitMQ queue "${process.env.RABBITMQ_USERS_QUEUE}"`,
    );
  } catch (error) {
    console.error('Error during application bootstrap: ', error);
    process.exit(1);
  }
}

void bootstrap();
