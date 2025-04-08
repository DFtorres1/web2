import { decode } from 'jsonwebtoken';
import { NotAcceptableException, NotFoundException } from '@nestjs/common';
import { TokenInterface } from 'src/modules/users/interfaces/token.interface';
import { User } from 'src/modules/users/user.entity';

export async function getUserFromAuthHeader(authHeader: string): Promise<User> {
  if (!authHeader || !authHeader.startsWith('Bearer')) {
    throw new NotAcceptableException('Authorization header is not valid');
  }

  const tokenMatch = authHeader.match(/^Bearer\s+(\S+)$/);
  const token = tokenMatch ? tokenMatch[1] : null;

  if (!token) {
    throw new NotFoundException('Authorization token not found');
  }

  const decodedToken: TokenInterface | null = decode(
    token,
  ) as TokenInterface | null;

  if (!decodedToken || !decodedToken.userId) {
    throw new NotFoundException('Invalid token: userId not found');
  }

  const userId: number = decodedToken.userId;

  const user = await this.usersRepository.findOneBy({ id: userId });

  if (!user) {
    throw new NotFoundException('User not found');
  }

  return user;
}
