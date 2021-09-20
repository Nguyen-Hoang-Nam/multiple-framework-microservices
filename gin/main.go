package main

import (
	"mlm.gin/discovery"
	"mlm.gin/router"
)

func main() {
	discovery.Init()

	router.Init()
}
