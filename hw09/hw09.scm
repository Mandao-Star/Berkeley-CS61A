(define (curry-cook formals body) 
    (if (null? (cdr formals))
               `(lambda (,(car formals)) ,body)
               `(lambda (,(car formals)) ,(curry-cook (cdr formals) body)))

    )

(define (curry-consume curry args)
    (if (null? args) 
        curry
        (curry-consume (curry (car args)) (cdr args)) )

  )

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
    (let [(expr (car (cdr switch-expr)))
          (options (car (cdr (cdr switch-expr))))]
        (cons 'cond
              (map (lambda (option) 
                       (list (list 'equal? expr (car option)) (car (cdr option))))
                   options))))
