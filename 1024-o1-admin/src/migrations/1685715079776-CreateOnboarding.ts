// import { generateEntityId } from "@medusajs/utils";
import { v4 as uuidv4 } from 'uuid';

const generateEntityId = () => uuidv4();
import { MigrationInterface, QueryRunner } from "typeorm";

export class CreateOnboarding1685715079776 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(
      `CREATE TABLE "onboarding_state" ("id" character varying NOT NULL, "created_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "updated_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "current_step" character varying NULL, "is_complete" boolean)`
    );

    await queryRunner.query(
      `INSERT INTO "onboarding_state" ("id", "current_step", "is_complete") VALUES ('${uuidv4()}', NULL, false)`
    );
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`DROP TABLE "onboarding_state"`);
  }
}
