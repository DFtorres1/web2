import { Controller, Inject } from '@nestjs/common';
import { UsersService } from '../providers/users.service';
import { ClientProxy, MessagePattern, Payload } from '@nestjs/microservices';
import { User } from '../user.entity';

@Controller()
export class UsersController {
  constructor(
    private readonly usersService: UsersService,
    @Inject('FASTAPI_SERVICE') private readonly fastapiClient: ClientProxy,
  ) {}

  @MessagePattern({ cmd: 'get_user_by_id' })
  async getUserById(@Payload() id: number): Promise<void> {
    console.log('ola');
    const data = await this.usersService.findOne(id);
    this.fastapiClient.emit('message_to_fastapi', data).subscribe()
  }
}
