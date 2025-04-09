import { Controller } from '@nestjs/common';
import { AuthService } from '../providers/auth.service';
import { LoginDto } from '../dto/login.dto';
import { RegisterDto } from '../dto/register.dto';
import { MessagePattern, Payload } from '@nestjs/microservices';

@Controller('auth')
export class AuthController {
  constructor(private readonly authService: AuthService) {}

  @MessagePattern({ cmd: 'login' })
  async login(
    @Payload() loginDto: LoginDto,
  ): Promise<{ token: string } | null> {
    return this.authService.login(loginDto);
  }

  @MessagePattern({ cmd: 'register' })
  async register(@Payload() registerDto: RegisterDto): Promise<void> {
    return this.authService.register(registerDto);
  }
}
