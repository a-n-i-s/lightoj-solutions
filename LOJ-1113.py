class Browser:
    """
    Responsible for simulating the browser behavior.
    
    Implement the methods as described in the problem.  
    """
    
    # Class variable to keep the default page loaded in the browser
    DEFAULT_PAGE = 'http://www.lightoj.com/'
    
    def __init__(self):
        """
        Initialize your data structures. If needed, keep the DEFAULT page as the initial page.
        """
        # Initialize your data structures
        self.backstack,self.frontstack=[],[]
        self.current=self.DEFAULT_PAGE



    def back(self) -> str:
        """
        If the backward stack is empty, return 'Ignored'.
        
        Otherwise, push the current page on the top of the forward stack. Also
        Pop the page from the top of the backward stack, making it the new current page.
        
        return the new current page.
        """
        # Implement the above logic
        if self.backstack==[]:
            return 'Ignored'
        self.frontstack.append(self.current)
        self.current=self.backstack.pop()
        return self.current
        
    def forward(self) -> str:
        """
        If the forward stack is empty, return 'Ignored'.
         
        Otherwise, push the current page on the top of the backward stack. Also
        Pop the page from the top of the forward stack, making it the new current page.
         
        return the new current page.
        """
        # Implement the above logic
        
        if self.frontstack==[]:
            return 'Ignored'
        self.backstack.append(self.current)
        self.current=self.frontstack.pop()
        return self.current

    def visit(self, url: str) -> str:
        """
        Push the current page on the top of the backward stack, and
        make the 'url' specified the new current page.
        
        The forward stack is also emptied.
        
        return the new current page.
        """
        # Implement the above logic

        self.backstack.append(self.current)
        self.current=url
        self.frontstack.clear()
        return url

def main():
    """
    Takes care of input and output.
    
    You don't have to make any changes here.
    """
    
    cases = int(input())
    for caseno in range(1, cases + 1):
        print('Case {}:'.format(caseno))
        
        browser = Browser()
        while True:
            command = input()
            if command == 'QUIT':
                break
            if command == 'BACK':
                print(browser.back())
            elif command == 'FORWARD':
                print(browser.forward())
            else:  # VISIT url
                _, url = command.split(' ', 2)
                print(browser.visit(url))

main()
