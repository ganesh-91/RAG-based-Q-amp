import { Controller, Get } from '@nestjs/common';

@Controller('health')
export class HealthController {
  @Get()
  checkHealth(): { status: string } {
    return { status: 'OK' }; // You can customize the response
  }
}
