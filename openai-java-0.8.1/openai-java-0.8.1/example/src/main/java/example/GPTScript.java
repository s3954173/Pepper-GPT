package example;

import com.theokanning.openai.OpenAiService;
import com.theokanning.openai.completion.CompletionRequest;
import com.theokanning.openai.completion.CompletionChoice;
import java.util.Scanner;

class GPTScript {
    public static void main(String... args) {
        // String token = System.getenv("OPENAI_TOKEN"); // trying to get the openai token from system
        OpenAiService service = new OpenAiService("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");
        Scanner sc = new Scanner(System.in);

        try {
            System.out.println("Hi, I'm Pepper. What can I help you with today?");

            boolean repeatInput = true;
            while (repeatInput == true) {
                System.out.print("User: ");
                String userInput = new String(sc.nextLine());

                if (userInput.toLowerCase().equals("exit")) {
                    System.out.println("Thanks for talking today!");
                    break;
                }

                CompletionRequest completionRequest = CompletionRequest.builder()
                        // .model("ada")
                        .model("text-davinci-003")
                        .prompt(userInput)
                        // .echo(true)
                        .user("testing")
                        .maxTokens(1024)
                        .temperature(0.5)
                        .n(1)
                        .build();
                CompletionChoice answer = service.createCompletion(completionRequest).getChoices().get(0); //.forEach(System.out::println);
                System.out.println("Pepper: " + answer.getText());
            }
        } finally {
            sc.close();
        }
    }
}
