package cmd

import (
	"fmt"
	"os"
	"path/filepath"

	"github.com/spf13/cobra"
)

var configureCmd = &cobra.Command{
	Use:   "configure",
	Short: "Configure credentials for accessing your S3 Bucket",
	Long:  ``,
	Run:   configure,
}

func configure(cmd *cobra.Command, args []string) {
	var accessKey string
	var secret string
	var region string

	// Get credentials via user input
	fmt.Println("Enter your Access Key ID:")
	fmt.Scanln(&accessKey)
	fmt.Println("Enter your Secret Access Key:")
	fmt.Scanln(&secret)
	fmt.Println("Enter the AWS Region your bucket is in:")
	fmt.Scanln(&region)

	// Make a directory for storing credentials
	home, err := os.UserHomeDir()
	if err != nil {
		fmt.Println("Unable to locate user's HOME directory")
	}
	dir := filepath.Join(home, ".bookly")
	err = os.MkdirAll(dir, os.ModePerm)
	if err != nil {
		fmt.Println("Making directory for config file failed: ", err)
	}

	// Create credentials file
	f, err := os.Create(home + "/.bookly/creds")
	if err != nil {
		fmt.Println("Unable to create credentials file: ", err)
	}

	// Write credentials to file
	bytes, err := f.WriteString(accessKey + "\n" + secret + "\n" + region)
	if bytes == 0 {
		fmt.Println("Wrote 0 bytes to file, please enter valid credentials")
	}
	if err != nil {
		fmt.Println("Error writing credentials to file: ", err)
	}
}

func init() {
	rootCmd.AddCommand(configureCmd)
}
