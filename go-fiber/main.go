package main

import (
	"app/item"

	"github.com/gofiber/fiber/v2"
)

func setupRoutes(app *fiber.App) {
	app.Get("/", item.GetItems)
	app.Get("/:id", item.GetItem)
	app.Post("/", item.NewItem)
	app.Put("/:id", item.UpdateItem)
	app.Delete("/:id", item.DeleteItem)
}

func main() {
	app := fiber.New()

	setupRoutes(app)

	app.Listen(":3000")
}
