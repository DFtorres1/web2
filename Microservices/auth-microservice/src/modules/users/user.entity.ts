import { Role } from 'src/common/enums/role.enum';
import { BaseEntity } from 'src/shared/interfaces/base.entity';
import { Column, Entity } from 'typeorm';

@Entity()
export class User extends BaseEntity {
  @Column()
  firstName: string;

  @Column()
  lastName: string;

  @Column({ unique: true })
  username: string;

  @Column()
  password: string;

  @Column({ type: 'enum', enum: Role, default: [Role.Tourist] })
  roles: Role[];
}
