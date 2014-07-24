import webapp2
import sudoku
import generator
import jinja2
import time
import random
import os

from google.appengine.ext import db
from google.appengine.api import taskqueue
from google.appengine.api import memcache

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class Puzzle(db.Model):
    start = db.StringProperty()
    values = db.StringProperty()
    number = db.IntegerProperty()
    level = db.StringProperty()
    
"""
Keep minimum one server instance running.
"""
    
class WakeHandler(webapp2.RequestHandler):
    def get(self):
        pass

"""
Schedule backend for puzzle generation.
"""    
class CronHandler(webapp2.RequestHandler):
    def get(self):
        taskqueue.add(url='/backend', target='1.backend')

"""
Manual puzzle generation using server frontend resources.
"""
class Cron2Handler(webapp2.RequestHandler):
    def get(self):
        taskqueue.add(url='/generate')
        taskqueue.add(url='/hard')
        taskqueue.add(url='/extreme')

"""
Add puzzles to memcache every 30 minutes to minimize maximum database lookups.
"""        
class CacheHandler(webapp2.RequestHandler):
    def get(self):
        memcache.flush_all()
        
        for i in range(50):
            total = Puzzle.all().filter('level =', 'Easy').order('-number').get()            
            number = random.randint(1, total.number)
            puzzle = Puzzle.all().filter('level =', 'Easy').filter('number =', number).get() #puzzle object
            string = 'Easy' + str(i)
            
            memcache.add('%s' % string, (puzzle.start, puzzle.values))
            
        for i in range(50):
            total = Puzzle.all().filter('level =', 'Medium').order('-number').get()            
            number = random.randint(1, total.number)
            puzzle = Puzzle.all().filter('level =', 'Medium').filter('number =', number).get() #puzzle object
            string = 'Medium' + str(i)
            
            memcache.add('%s' % string, (puzzle.start, puzzle.values))
        
        for i in range(50):
            total = Puzzle.all().filter('level =', 'Hard').order('-number').get()            
            number = random.randint(1, total.number)
            puzzle = Puzzle.all().filter('level =', 'Hard').filter('number =', number).get() #puzzle object
            string = 'Hard' + str(i)
            
            memcache.add('%s' % string, (puzzle.start, puzzle.values))
            
        for i in range(50):
            total = Puzzle.all().filter('level =', 'Extreme').order('-number').get()            
            number = random.randint(1, total.number)
            puzzle = Puzzle.all().filter('level =', 'Extreme').filter('number =', number).get() #puzzle object
            string = 'Extreme' + str(i)
            
            memcache.add('%s' % string, (puzzle.start, puzzle.values))
            
        
class GenerateHandler(webapp2.RequestHandler):
    def post(self):

        for i in range(1):
            initial, solution = generator.generate('Easy')
            while generator.easySort(initial) == False:
                initial, solution = generator.generate('Easy')
                
            latest = Puzzle.all().filter('level =', 'Easy').order('-number').get()
            if latest:
                number = latest.number + 1
            else:
                number = 1
           
            puzzle = Puzzle()
            puzzle.start = initial
            puzzle.values = solution
            puzzle.number = number
            puzzle.level = 'Easy'
            puzzle.put()
            
            initial, solution = generator.generate('Medium')
            while generator.mediumSort(initial) == False:
                initial, solution = generator.generate('Medium')
                
            latest = Puzzle.all().filter('level =', 'Medium').order('-number').get()
            if latest:
                number = latest.number + 1
            else:
                number = 1

            puzzle = Puzzle()
            puzzle.start = initial
            puzzle.values = solution
            puzzle.number = number
            puzzle.level = 'Medium'
            puzzle.put()

class HardHandler(webapp2.RequestHandler):
    def post(self):
        
        for i in range(1):
            initial, solution = generator.generate('Hard')
            while generator.hardSort(initial) == False:
                initial, solution = generator.generate('Hard')
                
            latest = Puzzle.all().filter('level =', 'Hard').order('-number').get()
            if latest:
                number = latest.number + 1
            else:
                number = 1

            puzzle = Puzzle()
            puzzle.start = initial
            puzzle.values = solution
            puzzle.number = number
            puzzle.level = 'Hard'
            puzzle.put()

class ExtremeHandler(webapp2.RequestHandler):
    def post(self):
        
        for i in range(1):
            initial, solution = generator.generate('Extreme')
            while generator.extremeSort(initial) == False:
                initial, solution = generator.generate('Extreme')
                
            latest = Puzzle.all().filter('level =', 'Extreme').order('-number').get()
            if latest:
                number = latest.number + 1
            else:
                number = 1
            
            puzzle = Puzzle()
            puzzle.start = initial
            puzzle.values = solution
            puzzle.number = number
            puzzle.level = 'Extreme'
            puzzle.put()

class BackendHandler(webapp2.RequestHandler):
    def post(self):
          
        for i in range(1):
            initial, solution = generator.generate('Easy')
            while generator.easySort(initial) == False:
                initial, solution = generator.generate('Easy')
                
            latest = Puzzle.all().filter('level =', 'Easy').order('-number').get()
            if latest:
                number = latest.number + 1
            else:
                number = 1
           
            puzzle = Puzzle()
            puzzle.start = initial
            puzzle.values = solution
            puzzle.number = number
            puzzle.level = 'Easy'
            puzzle.put()
            
            initial, solution = generator.generate('Medium')
            while generator.mediumSort(initial) == False:
                initial, solution = generator.generate('Medium')
                
            latest = Puzzle.all().filter('level =', 'Medium').order('-number').get()
            if latest:
                number = latest.number + 1
            else:
                number = 1

            puzzle = Puzzle()
            puzzle.start = initial
            puzzle.values = solution
            puzzle.number = number
            puzzle.level = 'Medium'
            puzzle.put()
                
        for i in range(1):
            initial, solution = generator.generate('Hard')
            while generator.hardSort(initial) == False:
                initial, solution = generator.generate('Hard')
                
            latest = Puzzle.all().filter('level =', 'Hard').order('-number').get()
            if latest:
                number = latest.number + 1
            else:
                number = 1

            puzzle = Puzzle()
            puzzle.start = initial
            puzzle.values = solution
            puzzle.number = number
            puzzle.level = 'Hard'
            puzzle.put()
            
        for i in range(1):
            initial, solution = generator.generate('Extreme')
            while generator.extremeSort(initial) == False:
                initial, solution = generator.generate('Extreme')
                
            latest = Puzzle.all().filter('level =', 'Extreme').order('-number').get()
            if latest:
                number = latest.number + 1
            else:
                number = 1
            
            puzzle = Puzzle()
            puzzle.start = initial
            puzzle.values = solution
            puzzle.number = number
            puzzle.level = 'Extreme'
            puzzle.put()

"""
View time samples in browser.  For debugging.
"""            
class TimeHandler(webapp2.RequestHandler):
    def get(self):
        dict_times = generator.timeSampler()
        average = {}
        minimum = {}
        maximum = {}
        times = {}

        for level in dict_times:
            average[level] = sum(dict_times[level]) / float(len(dict_times[level]))
            minimum[level] = min(dict_times[level])
            maximum[level] = max(dict_times[level])
            times[level] = dict_times[level]
            
        template_values = {
            'average' : average,
            'minimum' : minimum,
            'maximum' : maximum,
            'times' : times
        }
        
        template = jinja_environment.get_template('time.html')
        self.response.out.write(template.render(template_values))

"""
View partially solved puzzles in browser.  For debugging.
"""
class ValuesHandler(webapp2.RequestHandler):
    def get(self):
        multiple = []

        for i in range(10):
            initial, solution = generator.generate("Easy")
            solutions = []
            values = sudoku.parse_grid(initial)
            for i in range(10):
                list_values = []
                dict_values = sudoku.searchMultiple(values)
                for s in sudoku.squares:
                    list_values.append(dict_values[s])
                solution = "".join(list_values)
                solutions.append(solution)
            multiple.append(len(set(solutions)))

        for i in range(10):
            initial, solution = generator.generate("Medium")
            solutions = []
            values = sudoku.parse_grid(initial)
            for i in range(10):
                list_values = []
                dict_values = sudoku.searchMultiple(values)
                for s in sudoku.squares:
                    list_values.append(dict_values[s])
                solution = "".join(list_values)
                solutions.append(solution)
            multiple.append(len(set(solutions)))
        
        for i in range(10):
            initial, solution = generator.generate("Hard")
            solutions = []
            values = sudoku.parse_grid(initial)
            for i in range(10):
                list_values = []
                dict_values = sudoku.searchMultiple(values)
                for s in sudoku.squares:
                    list_values.append(dict_values[s])
                solution = "".join(list_values)
                solutions.append(solution)
            multiple.append(len(set(solutions)))

        for i in range(10):
            initial, solution = generator.generate("Extreme")
            solutions = []
            values = sudoku.parse_grid(initial)
            for i in range(10):
                list_values = []
                values = sudoku.parse_grid(initial)
                dict_values = sudoku.searchMultiple(values)
                for s in sudoku.squares:
                    list_values.append(dict_values[s])
                solution = "".join(list_values)
                solutions.append(solution)
            multiple.append(len(set(solutions)))
            


        template_values = {
            'multiple' : multiple
        }

        template = jinja_environment.get_template('values.html')
        self.response.out.write(template.render(template_values))
        
"""
Enter any puzzle to check parameters.  For debugging.
"""
class MeasureHandler(webapp2.RequestHandler):
    def get(self):
        easy = ['8..5.2.6..2...358.....1.7427....125.5.......7.187....6682.9.....318...9..5.4.6..8',
                '3..76...2..9.5..6...2.9...42.74...36..16.92..69...54.75...4.3...1..3.7..7...12..9',
                '8.4..5.2...6.8....75192.38..4.6.....9.8.4.1.2.....2.7..15.69238....5.7...2.4..9.5',
                '4.37..65....9.4.71..1..543.3...9..26...6.1...67..8...4.863..7..23.1.6....57..81.3',
                '...76..9.....917.2.....46...13.8.24.8.6.4.3.5.54.7.86...79.....6.152.....2..38...',
                '2..6..34.....5...93..72.861..3.627.....8.7.....613.4..785.93..61...7.....69..1..7',
                '..54.3...8.6..243.37.......56....7.974.591.239.3....18.......96.826..1.7...1.72..']

        medium = ['.7..6.34...25.9..7..1..4...7.81....4.........5....71.2...4..6..3..6.85...56.9..1.',
                  '.524.....1..9..8..8...63.179.....6....81467....6.....448.61...9..1..7..6.....415.',
                  '9.2........4.5.78.........36..2...9521.9.3.7849...7..61.........83.9.2........8.1',
                  '..2.4...5.4.325..6.5...79.4.....247....5.4....987.....7.48...6.3..456.1.5...7.3..',
                  '4...9..8..5.4.....98.1....78..67..2..2.....1..1..59..61....4.59.....2.3..3..6...4',
                  '.8..6.43...4..1.8..934......3..287..6.......2..751..6......589..7.1..5...25.4..7.',
                  '31.2..5............24.61.3784...91......8......73...6447.69.35............5..4.18']
        
        hard = ['3....9.86..6.18.4.....6.5..5.....62.2..531..4.87.....5..5.2.....2.97.3..79.3....2',
                '.62..5...4...71.861.......26..89.2..82.....95..1.27..83.......459.34...7...7..96.',
                '.89..3.2...5.....4...1.95..95.62.3..6.......8..7.15.62..38.4...4.....8...9.7..64.']
        
        extreme = ['2.1.8...5.3.7........1...9...5.4.73.4.75.16.9.86.9.5...4...2........6.7.6...7.2.8',
                   '375..1....8..2.5.3..193....8.....1.7...3.2...1.3.....4....543..5.9.6..8....1..456',
                   '8.735....5......8..91.2..4.4.....5...569.142...3.....6.4..6.13..7......4....489.7']

        e_singles = []
        e_solutions = []
        for p in easy:
            grid = sudoku.parse_grid(p)

            solved = 0
            for s in grid:
                if len(grid[s]) == 1:
                    solved += 1
            e_singles.append(solved)

            solutions = []
            for i in range(10):
                list_values = []
                dict_values = sudoku.searchMultiple(grid)
                for s in sudoku.squares:
                    list_values.append(dict_values[s])
                solution = "".join(list_values)
                solutions.append(solution)
            e_solutions.append(len(set(solutions)))

        m_singles = []
        m_solutions = []
        for p in medium:
            grid = sudoku.parse_grid(p)

            solved = 0
            for s in grid:
                if len(grid[s]) == 1:
                    solved += 1
            m_singles.append(solved)

            solutions = []
            for i in range(10):
                list_values = []
                dict_values = sudoku.searchMultiple(grid)
                for s in sudoku.squares:
                    list_values.append(dict_values[s])
                solution = "".join(list_values)
                solutions.append(solution)
            m_solutions.append(len(set(solutions)))

        h_singles = []
        h_solutions = []
        for p in hard:
            grid = sudoku.parse_grid(p)

            solved = 0
            for s in grid:
                if len(grid[s]) == 1:
                    solved += 1
            h_singles.append(solved)

            solutions = []
            for i in range(30):
                list_values = []
                dict_values = sudoku.searchMultiple(grid)
                for s in sudoku.squares:
                    list_values.append(dict_values[s])
                solution = "".join(list_values)
                solutions.append(solution)
            h_solutions.append(len(set(solutions)))

        ex_singles = []
        ex_solutions = []
        for p in extreme:
            grid = sudoku.parse_grid(p)

            solved = 0
            for s in grid:
                if len(grid[s]) == 1:
                    solved += 1
            ex_singles.append(solved)

            solutions = []
            for i in range(30):
                list_values = []
                dict_values = sudoku.searchMultiple(grid)
                for s in sudoku.squares:
                    list_values.append(dict_values[s])
                solution = "".join(list_values)
                solutions.append(solution)
            ex_solutions.append(len(set(solutions)))

        template_values = {
            'e_singles' : e_singles,
            'm_singles' : m_singles,
            'h_singles' : h_singles,
            'ex_singles' : ex_singles,
            'e_solutions' : e_solutions,
            'm_solutions' : m_solutions,
            'h_solutions' : h_solutions,
            'ex_solutions' : ex_solutions
        }

        template = jinja_environment.get_template('measure.html')
        self.response.out.write(template.render(template_values))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render())
        
class StrategyHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('strategy.html')
        self.response.out.write(template.render())

"""
Close Facebook dialog popup.
"""    
class CloseHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('close.html')
        self.response.out.write(template.render())

"""
Sample puzzles for solvability.  For debugging.
"""        
class SampleHandler(webapp2.RequestHandler):
    def get(self):
        hard_samples = []
        h_singles = []
    
        for i in range(10):
            total = Puzzle.all().filter('level =', 'Hard').order('-number').get()
            number = random.randint(1, total.number)
            hard = Puzzle.all().filter('level =', 'Hard').filter('number =', number).get()
            values = sudoku.parse_grid(hard.start)
        
            solved = 0
            for s in values:
                if len(values[s]) == 1:
                    solved += 1
            h_singles.append(solved)
        
            solutions = []
            for i in range(99):
                list_values = []
                dict_values = sudoku.searchMultiple(values)
                for s in sudoku.squares:
                    list_values.append(dict_values[s])
                solution = "".join(list_values)
                solutions.append(solution)
        
            hard_samples.append(len(set(solutions)))
    
        extreme_samples = []
        ex_singles = []
    
        for i in range(10):
            total = Puzzle.all().filter('level =', 'Extreme').order('-number').get()
            number = random.randint(1, total.number)
            extreme = Puzzle.all().filter('level =', 'Extreme').filter('number =', number).get()
            values = sudoku.parse_grid(extreme.start)
        
            solved = 0
            for s in values:
                if len(values[s]) == 1:
                    solved += 1
            ex_singles.append(solved)
        
            solutions = []
            for i in range(99):
                list_values = []
                dict_values = sudoku.searchMultiple(values)
                for s in sudoku.squares:
                    list_values.append(dict_values[s])
                solution = "".join(list_values)
                solutions.append(solution)
        
            extreme_samples.append(len(set(solutions)))
        
        template_values = {
                            'h_singles' : h_singles,
                            'ex_singles' : ex_singles,
                            'hard_samples' : hard_samples,
                            'extreme_samples' : extreme_samples
                            }
        
        template = jinja_environment.get_template('sample.html')
        self.response.out.write(template.render(template_values))

"""
Serve main page.
"""        
class SudokuHandler(webapp2.RequestHandler):
    def get(self):
        level = self.request.get("level") #get level and number from query
        number = self.request.get("number")
        if number.isdigit():
            number = int(number)
        else:
            number = None
        if not level: level = 'Medium' #if no level query, default Medium
            
        if number==None: #if no number query, get random puzzle from memcache
            number = random.randint(0, 49)
            tup = (level, number)
            string = level + str(number)
            puzzle = memcache.get('%s' % string)
            
            if puzzle is not None:
                initial = dict(zip(sudoku.squares, puzzle[0]))
                solution = puzzle[1]
            else:
                number = None
                initial, solution, level, number = self.get_from_database(level, number) # if not in memcache, pull from database
        else:
            initial, solution, level, number = self.get_from_database(level, number)

        template_values = {
            'start': initial,
            'solution': solution,
            'level' : level,
            'number' : number
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))
        
    def get_from_database(self, level, number):
        test = Puzzle.all().get() #test if there are database entries
        if test:
            total = Puzzle.all().filter('level =', level).order('-number').get()
            if number==None or number > total.number: #if no number query, get random puzzle               
                number = random.randint(1, total.number)
            puzzle = Puzzle.all().filter('level =', level).filter('number =', number).get() #puzzle object

            initial = dict(zip(sudoku.squares, puzzle.start))
            #solution = dict(zip(sudoku.squares, puzzle.values))
            solution = puzzle.values
            level = puzzle.level
            number = puzzle.number
            
            return initial, solution, level, number

        else:
            sample_start = '85...24..72......9..4.........1.7..23.5...9...4...........8..7..17..........36.4.'
            sample_values = '859612437723854169164379528986147352375268914241593756432981675617425893598736241'

            initial = dict(zip(sudoku.squares, sample_start))
            #solution = dict(zip(sudoku.squares, sample_values))
            solution = sample_values
            level = 'Hard'
            number = 1
            
            return initial, solution, level, number

"""
Serve widget.
"""        
class MiniHandler(webapp2.RequestHandler):
    def get(self):
        level = self.request.get("level") #get level and number from query
        number = self.request.get("number")
        if number.isdigit():
            number = int(number)
        else:
            number = None
        if not level: level = 'Easy' #if no level query, default Easy
            
        if number==None: #if no number query, get random puzzle from memcache
            number = random.randint(0, 49)
            tup = (level, number)
            string = level + str(number)
            puzzle = memcache.get('%s' % string)
            
            if puzzle is not None:
                initial = dict(zip(sudoku.squares, puzzle[0]))
                solution = puzzle[1]
            else:
                number = None
                initial, solution, level, number = self.get_from_database(level, number)
        else:
            initial, solution, level, number = self.get_from_database(level, number)

        template_values = {
            'start': initial,
            'solution': solution,
            'level' : level,
            'number' : number
        }

        template = jinja_environment.get_template('mini.html')
        self.response.out.write(template.render(template_values))
        
    def get_from_database(self, level, number):
        test = Puzzle.all().get() #test if there are database entries
        if test:
            total = Puzzle.all().filter('level =', level).order('-number').get()
            if number==None or number > total.number: #if no number query, get random puzzle               
                number = random.randint(1, total.number)
            puzzle = Puzzle.all().filter('level =', level).filter('number =', number).get() #puzzle object

            initial = dict(zip(sudoku.squares, puzzle.start))
            #solution = dict(zip(sudoku.squares, puzzle.values))
            solution = puzzle.values
            level = puzzle.level
            number = puzzle.number
            
            return initial, solution, level, number

        else:
            sample_start = '85...24..72......9..4.........1.7..23.5...9...4...........8..7..17..........36.4.'
            sample_values = '859612437723854169164379528986147352375268914241593756432981675617425893598736241'

            initial = dict(zip(sudoku.squares, sample_start))
            #solution = dict(zip(sudoku.squares, sample_values))
            solution = sample_values
            level = 'Hard'
            number = 1
            
            return initial, solution, level, number
        
class WidgetHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('widget.html')
        self.response.out.write(template.render())
        
app = webapp2.WSGIApplication([('/', SudokuHandler),
                               ('/wake', WakeHandler),
                               ('/cron', CronHandler),
                               ('/cron2', Cron2Handler),
                               ('/cache', CacheHandler),
                               ('/generate', GenerateHandler),
                               ('/hard', HardHandler),
                               ('/extreme', ExtremeHandler),
                               ('/backend', BackendHandler),
                               ('/time', TimeHandler),
                               ('/values', ValuesHandler),
                               ('/measure', MeasureHandler),
                               ('/about', AboutHandler),
                               ('/strategy', StrategyHandler),
                               ('/close', CloseHandler),
                               ('/sample', SampleHandler),
                               ('/mini', MiniHandler),
                               ('/widget', WidgetHandler)
                              ], debug=True)
