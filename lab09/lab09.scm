(define (over-or-under num1 num2) 
        (cond
          [(= num1 num2) 0]
          [(< num1 num2) -1]
          [(> num1 num2) 1]
          ))

(define (make-adder num) 
        (lambda (inc)
          (+ num inc))
)

(define (composed f g) 
      (lambda (x) 
        (f (g x)))
)

(define (repeat f n)
      (if (= n 1)
        f
        (composed f (repeat f (- n 1))))
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
      (if (zero? b) 
        a
        (gcd b (modulo a b)))
)
