import { Global, Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { ClientsModule, Transport } from '@nestjs/microservices';

@Global()
@Module({
  imports: [
    ConfigModule,
    ClientsModule.registerAsync([
      {
        name: 'FASTAPI_SERVICE',
        useFactory: () => ({
          transport: Transport.RMQ,
          options: {
            urls: process.env.RABBITMQ_URI?.split(','),
            queue: process.env.RABBITMQ_FASTAPI_QUEUE,
            queueOptions: {
              durable: true,
            },
          },
        }),
      },
    ]),
  ],
  exports: [ClientsModule],
})
export class RabbitMQModule {}
