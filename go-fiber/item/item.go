package item

import "github.com/gofiber/fiber/v2"

func GetItem(c *fiber.Ctx) error {
	return c.SendString("Get Item")
}

func GetItems(c *fiber.Ctx) error {
	return c.SendString("All Items")
}

func NewItem(c *fiber.Ctx) error {
	return c.SendString("New Item")
}

func UpdateItem(c *fiber.Ctx) error {
	return c.SendString("Update Item")
}

func DeleteItem(c *fiber.Ctx) error {
	return c.SendString("Delete Item")
}
