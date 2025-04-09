import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { TypeOrmModule } from '@nestjs/typeorm';
import { UsersRMQModule } from './modules/users/usersrmq.module';
import { RabbitMQModule } from './modules/rabbitmq/rabbitmq.module';

@Module({
  imports: [
    UsersRMQModule,
    RabbitMQModule,
    ConfigModule.forRoot(),
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: process.env.DATABASE_HOST,
      port: +(process.env.DATABASE_PORT || 5432),
      username: process.env.DATABASE_USER,
      password: process.env.DATABASE_PASSWORD,
      database: process.env.DATABASE_NAME,
      entities: [__dirname + './**/*.entity{.ts,.js}'],
      synchronize: false,
      autoLoadEntities: true
    })
  ],
})
export class AppModule { }
