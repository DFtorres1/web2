import { Global, Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { ClientsModule, Transport } from '@nestjs/microservices';

@Global()
@Module({
  imports: [
    ConfigModule,
    ClientsModule.registerAsync([
      {
        name: 'USERS_SERVICE',
        useFactory: () => ({
          transport: Transport.RMQ,
          options: {
            urls: process.env.RABBITMQ_URI?.split(','),
            queue: process.env.RABBITMQ_USERS_QUEUE,
            queueOptions: {
              durable: false,
            },
          },
        }),
      },
    ]),
  ],
  exports: ['USERS_SERVICE'],
})
export class RabbitMQModule {}
