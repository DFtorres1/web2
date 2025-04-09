import { Module } from '@nestjs/common';
import { AuthService } from './providers/auth.service';
import { UsersService } from './providers/users.service';
import { UsersModule } from './users.module';
import { AuthController } from './controllers/auth.controller';
import { UsersController } from './controllers/users.controller';

@Module({
  imports: [UsersModule],
  controllers: [AuthController, UsersController],
  providers: [AuthService, UsersService],
  exports: [AuthService, UsersService],
})
export class UsersRMQModule {}
