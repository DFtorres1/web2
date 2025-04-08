import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { MicroserviceOptions, Transport } from '@nestjs/microservices';

async function bootstrap() {
  try {
    const app = await NestFactory.createMicroservice<MicroserviceOptions>(
      AppModule,
      {
        transport: Transport.NATS,
        options: {
          host: process.env.BACKEND_URL,
          port: process.env.PORT ?? 3000,
        },
      },
    );
    // app.enableCors({
    //   origin: process.env.FRONTEND_URL,
    //   methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
    //   credentials: true,
    // });
    await app.listen();
    console.log(`Application running on: ${await 30}`);
  } catch (error) {
    console.error('Error during application bootstrap: ', error);
    process.exit(1);
  }
}

void bootstrap();
