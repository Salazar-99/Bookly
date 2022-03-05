package cmd

import (
	"os"

	"github.com/spf13/cobra"
)

// Base command
var rootCmd = &cobra.Command{
	Use:   "bookly",
	Short: "Bookly is a CLI tool for managing blog posts stored in AWS S3",
	Long:  `Bookly is a CLI tool for managing blog posts stored in AWS S3`,
}

func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}

func init() {
	// Here you will define your flags and configuration settings.
	// Cobra supports persistent flags, which, if defined here,
	// will be global for your application.

	// rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is $HOME/.Bookly.yaml)")

	// Cobra also supports local flags, which will only run
	// when this action is called directly.
	rootCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}
