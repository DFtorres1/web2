import { Module } from '@nestjs/common';
import { AuthService } from './providers/auth.service';
import { UsersService } from './providers/users.service';
import { UsersModule } from './users.module';
import { AuthController } from './controllers/auth.controller';

@Module({
  imports: [UsersModule],
  controllers: [AuthController],
  providers: [UsersService, AuthService],
  exports: [AuthService],
})
export class UsersHttpModule {}
