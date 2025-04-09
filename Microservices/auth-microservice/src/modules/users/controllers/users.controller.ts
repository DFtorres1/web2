import { Controller } from "@nestjs/common";
import { UsersService } from "../providers/users.service";
import { MessagePattern, Payload } from "@nestjs/microservices";
import { User } from "../user.entity";

@Controller()
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @MessagePattern({ cmd: 'get_user_by_id' })
  getUserById(@Payload() id: number): Promise<User | null> {
    console.log("ola")
    return this.usersService.findOne(id);
  }
}
