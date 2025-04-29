


(define p (cons 1 2))
p       ; → (1 . 2)
(car p) ; → 1
(cdr p) ; → 2

(define lst (cons 1 (cons 2 '())))
lst     ; → (1 2) （等价于 (1 . (2 . ()))）