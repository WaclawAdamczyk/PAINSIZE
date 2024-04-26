#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Fri Apr 26 00:54:09 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from preSettings
from datetime import datetime
# Get the current date and time
current_datetime = datetime.now()
# Format the date and time as 'yyyymmddhhmmss'
formatted_date = current_datetime.strftime('%Y%m%d%H%M%S')
# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'painSizeTask'  # from the Builder filename that created this script
expInfo = {
    'subjectID': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'%s/%s_%s_%s' % (expInfo['subjectID'], expInfo['subjectID'], expName, formatted_date)
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/vatsi/RESEARCH/PAINSIZE_20240305/painSize_GitHub/painSize_v9_scalePractice_18082022.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.DEBUG)


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1512, 982], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color='black', colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='cm'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = 'black'
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'cm'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Setings" ---
    keyStart = keyboard.Keyboard()
    # Run 'Begin Experiment' code from preSettings
    
    #take all libraries needed for the study
    import random
    import time
    from psychopy.tools.filetools import fromFile, toFile#no idea why but it is a neccessity
    from painSize_instructions_20240425 import size_PainTask, size_PainInstr, intens_PainTask, intens_PainLeft, intens_PainRight, intens_PainInstr
    from painSize_instructions_20240425 import unp_PainTask, unp_PainLeft, unp_PainRight, unp_PainInstr
    from painSize_instructions_20240425 import beginPractice, size_PainPractice, intens_unp_PainPractice
    intX=(-7.5)
    test_start = core.monotonicClock.getTime()
    ISI = 2
    time.sleep(2)#that lapse is crucial to laod all of the packages
    
    txtStart = visual.TextStim(win=win, name='txtStart',
        text=None,
        font='Arial',
        pos=None, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "PAIN_size" ---
    SizeMouse = event.Mouse(win=win)
    x, y = [None, None]
    SizeMouse.mouseClock = core.Clock()
    ThermodeRect = visual.Rect(
        win=win, name='ThermodeRect',units='cm', 
        width=(1.6, 1.6)[0], height=(1.6, 1.6)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-2.0, interpolate=True)
    PainRect = visual.Rect(
        win=win, name='PainRect',units='cm', 
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=(0,0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=-3.0, interpolate=True)
    rateS = visual.TextStim(win=win, name='rateS',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color=None, colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    rateInstruction = visual.TextStim(win=win, name='rateInstruction',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='cyan', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "PAIN_int" ---
    ratePain = visual.TextStim(win=win, name='ratePain',
        text=None,
        font='Arial',
        units='cm', pos=(0,9), height=1.5, wrapWidth=20.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    noPain = visual.TextStim(win=win, name='noPain',
        text=None,
        font='Open Sans',
        units='cm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    maxPain = visual.TextStim(win=win, name='maxPain',
        text=None,
        font='Open Sans',
        units='cm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    red_int = visual.Rect(
        win=win, name='red_int',units='cm', 
        width=(15,3)[0], height=(15,3)[1],
        ori=0.0, pos=(intX,0), anchor='center',
        lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='red',
        opacity=1.0, depth=-3.0, interpolate=True)
    white_int = visual.Rect(
        win=win, name='white_int',units='cm', 
        width=(15,3)[0], height=(15,3)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    leftTr = visual.ShapeStim(
        win=win, name='leftTr',units='cm', 
        size=(0.3, 0.3), vertices='triangle',
        ori=180.0, pos=(-15.0, 2.0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    rightTri = visual.ShapeStim(
        win=win, name='rightTri',units='cm', 
        size=(0.3, 0.3), vertices='triangle',
        ori=180.0, pos=(0, 2.0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    MouseInt = event.Mouse(win=win)
    x, y = [None, None]
    MouseInt.mouseClock = core.Clock()
    intensInstruction = visual.TextStim(win=win, name='intensInstruction',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    
    # --- Initialize components for Routine "PAIN_unp" ---
    rateUnp = visual.TextStim(win=win, name='rateUnp',
        text=None,
        font='Arial',
        units='cm', pos=(0,9), height=1.5, wrapWidth=25.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    noUnp = visual.TextStim(win=win, name='noUnp',
        text=None,
        font='Open Sans',
        units='cm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    maxUnp = visual.TextStim(win=win, name='maxUnp',
        text=None,
        font='Open Sans',
        units='cm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    red_Unp = visual.Rect(
        win=win, name='red_Unp',units='cm', 
        width=(15,3)[0], height=(15,3)[1],
        ori=0.0, pos=(intX,0), anchor='center',
        lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='red',
        opacity=1.0, depth=-3.0, interpolate=True)
    white_Unp = visual.Rect(
        win=win, name='white_Unp',units='cm', 
        width=(15,3)[0], height=(15,3)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    leftAr = visual.ShapeStim(
        win=win, name='leftAr',units='cm', 
        size=(0.3, 0.3), vertices='triangle',
        ori=180.0, pos=(-15.0, 2.0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    rightAr = visual.ShapeStim(
        win=win, name='rightAr',units='cm', 
        size=(0.3, 0.3), vertices='triangle',
        ori=180.0, pos=(0, 2.0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    MouseUnp = event.Mouse(win=win)
    x, y = [None, None]
    MouseUnp.mouseClock = core.Clock()
    unpInstruction = visual.TextStim(win=win, name='unpInstruction',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    
    # --- Initialize components for Routine "Closing" ---
    textEnd = visual.TextStim(win=win, name='textEnd',
        text=None,
        font='Arial',
        pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyEnding = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "Setings" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Setings.started', globalClock.getTime())
    keyStart.keys = []
    keyStart.rt = []
    _keyStart_allKeys = []
    # Run 'Begin Routine' code from preSettings
    #Preliminary instruction
    txtStart = visual.TextStim(win, beginPractice,
                           color=(255,255,255), colorSpace='rgb', alignText='center',units='cm', pos=(0,0), height=0.8, wrapWidth=30)
    
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    SetingsComponents = [keyStart, txtStart, mouse]
    for thisComponent in SetingsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Setings" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *keyStart* updates
        waitOnFlip = False
        
        # if keyStart is starting this frame...
        if keyStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyStart.frameNStart = frameN  # exact frame index
            keyStart.tStart = t  # local t and not account for scr refresh
            keyStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyStart, 'tStartRefresh')  # time at next scr refresh
            # update status
            keyStart.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyStart.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyStart.status == STARTED and not waitOnFlip:
            theseKeys = keyStart.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyStart_allKeys.extend(theseKeys)
            if len(_keyStart_allKeys):
                keyStart.keys = _keyStart_allKeys[-1].name  # just the last key pressed
                keyStart.rt = _keyStart_allKeys[-1].rt
                keyStart.duration = _keyStart_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from preSettings
        win.mouseVisible = False
        
        # *txtStart* updates
        
        # if txtStart is starting this frame...
        if txtStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txtStart.frameNStart = frameN  # exact frame index
            txtStart.tStart = t  # local t and not account for scr refresh
            txtStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txtStart, 'tStartRefresh')  # time at next scr refresh
            # update status
            txtStart.status = STARTED
            txtStart.setAutoDraw(True)
        
        # if txtStart is active this frame...
        if txtStart.status == STARTED:
            # update params
            pass
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse is stopping this frame...
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse.stopped', t)
                # update status
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SetingsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Setings" ---
    for thisComponent in SetingsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Setings.stopped', globalClock.getTime())
    # check responses
    if keyStart.keys in ['', [], None]:  # No response was made
        keyStart.keys = None
    thisExp.addData('keyStart.keys',keyStart.keys)
    if keyStart.keys != None:  # we had a response
        thisExp.addData('keyStart.rt', keyStart.rt)
        thisExp.addData('keyStart.duration', keyStart.duration)
    thisExp.nextEntry()
    # store data for thisExp (ExperimentHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    thisExp.addData('mouse.x', x)
    thisExp.addData('mouse.y', y)
    thisExp.addData('mouse.leftButton', buttons[0])
    thisExp.addData('mouse.midButton', buttons[1])
    thisExp.addData('mouse.rightButton', buttons[2])
    thisExp.nextEntry()
    # the Routine "Setings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loopSize = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loopSize')
    thisExp.addLoop(loopSize)  # add the loop to the experiment
    thisLoopSize = loopSize.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopSize.rgb)
    if thisLoopSize != None:
        for paramName in thisLoopSize:
            globals()[paramName] = thisLoopSize[paramName]
    
    for thisLoopSize in loopSize:
        currentLoop = loopSize
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisLoopSize.rgb)
        if thisLoopSize != None:
            for paramName in thisLoopSize:
                globals()[paramName] = thisLoopSize[paramName]
        
        # --- Prepare to start Routine "PAIN_size" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('PAIN_size.started', globalClock.getTime())
        # setup some python lists for storing info about the SizeMouse
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from SizeCode
        #Mouse settings here:
        intX=1
        SizeMouse.setPos((0,0))
        #Setup the text displayed in the screen
        #Task to participant
        rateS = visual.TextStim(win, size_PainTask,
                               color='white', colorSpace='rgb', alignText='center',units='cm', pos=(0,9), height=1.5, wrapWidth=30)
        #Instruction
        rateInstruction = visual.TextStim(win, size_PainInstr,
                               color='white', colorSpace='rgb', alignText='center',units='cm', pos=(0,-9), height=0.6, wrapWidth=30)
        # keep track of which components have finished
        PAIN_sizeComponents = [SizeMouse, ThermodeRect, PainRect, rateS, rateInstruction]
        for thisComponent in PAIN_sizeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PAIN_size" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *SizeMouse* updates
            
            # if SizeMouse is starting this frame...
            if SizeMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SizeMouse.frameNStart = frameN  # exact frame index
                SizeMouse.tStart = t  # local t and not account for scr refresh
                SizeMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SizeMouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('SizeMouse.started', t)
                # update status
                SizeMouse.status = STARTED
                SizeMouse.mouseClock.reset()
                prevButtonState = SizeMouse.getPressed()  # if button is down already this ISN'T a new click
            if SizeMouse.status == STARTED:  # only update if started and not finished!
                buttons = SizeMouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # end routine on response            # Run 'Each Frame' code from SizeCode
            #white_rect.setPos((mouse.getPos()[0],0), log=False)
            currentPosI = SizeMouse.getPos()
            xPosI = currentPosI[0]
            xSize = abs(xPosI)
            intX = xSize
            win.mouseVisible = False
            
            # *ThermodeRect* updates
            
            # if ThermodeRect is starting this frame...
            if ThermodeRect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ThermodeRect.frameNStart = frameN  # exact frame index
                ThermodeRect.tStart = t  # local t and not account for scr refresh
                ThermodeRect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ThermodeRect, 'tStartRefresh')  # time at next scr refresh
                # update status
                ThermodeRect.status = STARTED
                ThermodeRect.setAutoDraw(True)
            
            # if ThermodeRect is active this frame...
            if ThermodeRect.status == STARTED:
                # update params
                pass
            
            # *PainRect* updates
            
            # if PainRect is starting this frame...
            if PainRect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PainRect.frameNStart = frameN  # exact frame index
                PainRect.tStart = t  # local t and not account for scr refresh
                PainRect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PainRect, 'tStartRefresh')  # time at next scr refresh
                # update status
                PainRect.status = STARTED
                PainRect.setAutoDraw(True)
            
            # if PainRect is active this frame...
            if PainRect.status == STARTED:
                # update params
                PainRect.setSize((intX,intX), log=False)
            
            # *rateS* updates
            
            # if rateS is starting this frame...
            if rateS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rateS.frameNStart = frameN  # exact frame index
                rateS.tStart = t  # local t and not account for scr refresh
                rateS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rateS, 'tStartRefresh')  # time at next scr refresh
                # update status
                rateS.status = STARTED
                rateS.setAutoDraw(True)
            
            # if rateS is active this frame...
            if rateS.status == STARTED:
                # update params
                pass
            
            # *rateInstruction* updates
            
            # if rateInstruction is starting this frame...
            if rateInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rateInstruction.frameNStart = frameN  # exact frame index
                rateInstruction.tStart = t  # local t and not account for scr refresh
                rateInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rateInstruction, 'tStartRefresh')  # time at next scr refresh
                # update status
                rateInstruction.status = STARTED
                rateInstruction.setAutoDraw(True)
            
            # if rateInstruction is active this frame...
            if rateInstruction.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PAIN_sizeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PAIN_size" ---
        for thisComponent in PAIN_sizeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('PAIN_size.stopped', globalClock.getTime())
        # store data for loopSize (TrialHandler)
        x, y = SizeMouse.getPos()
        buttons = SizeMouse.getPressed()
        loopSize.addData('SizeMouse.x', x)
        loopSize.addData('SizeMouse.y', y)
        loopSize.addData('SizeMouse.leftButton', buttons[0])
        loopSize.addData('SizeMouse.midButton', buttons[1])
        loopSize.addData('SizeMouse.rightButton', buttons[2])
        # Run 'End Routine' code from SizeCode
        #what is the postion of cursor?
        mouse_click = SizeMouse.getPos()
        #what was the last 'x' coordinate?
        x_clickS = abs(mouse_click[0])
        #calculate the surface and save with 3 decimal
        painSize = round(x_clickS*x_clickS,3)
        #save data
        loopSize.addData('Size_Rating', painSize)#was thisExp
        loopSize.addData('Size_Rating_duration(sec)', t)
        # the Routine "PAIN_size" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "PAIN_int" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('PAIN_int.started', globalClock.getTime())
        # setup some python lists for storing info about the MouseInt
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from IntCode
        #Mouse settings
        intX=-7.5
        MouseInt.setPos((-7.5,0))
        
        #Task
        ratePain = visual.TextStim(win,intens_PainTask,
        color='white', colorSpace='rgb', alignText='center',units='cm', pos=(0,9), height=1.3, wrapWidth=35)
        
        #Left anchor of VAS
        noPain = visual.TextStim(win, intens_PainLeft, color='white', colorSpace='rgb',
        alignText='center', units='cm', pos=(-16,3), height=0.5)
        
        #Right anchor of VAS
        maxPain = visual.TextStim(win, intens_PainRight, color='white', colorSpace='rgb',
        alignText='center', units='cm', pos=(2,3), height=0.5)
        
        #VAS instruction
        intensInstruction = visual.TextStim(win, intens_PainInstr,
                               color='white', colorSpace='rgb', alignText='center',units='cm', pos=(0,-9), height=0.6, wrapWidth=16)
        
        # keep track of which components have finished
        PAIN_intComponents = [ratePain, noPain, maxPain, red_int, white_int, leftTr, rightTri, MouseInt, intensInstruction]
        for thisComponent in PAIN_intComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PAIN_int" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ratePain* updates
            
            # if ratePain is starting this frame...
            if ratePain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratePain.frameNStart = frameN  # exact frame index
                ratePain.tStart = t  # local t and not account for scr refresh
                ratePain.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratePain, 'tStartRefresh')  # time at next scr refresh
                # update status
                ratePain.status = STARTED
                ratePain.setAutoDraw(True)
            
            # if ratePain is active this frame...
            if ratePain.status == STARTED:
                # update params
                pass
            
            # *noPain* updates
            
            # if noPain is starting this frame...
            if noPain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                noPain.frameNStart = frameN  # exact frame index
                noPain.tStart = t  # local t and not account for scr refresh
                noPain.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noPain, 'tStartRefresh')  # time at next scr refresh
                # update status
                noPain.status = STARTED
                noPain.setAutoDraw(True)
            
            # if noPain is active this frame...
            if noPain.status == STARTED:
                # update params
                pass
            
            # *maxPain* updates
            
            # if maxPain is starting this frame...
            if maxPain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                maxPain.frameNStart = frameN  # exact frame index
                maxPain.tStart = t  # local t and not account for scr refresh
                maxPain.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(maxPain, 'tStartRefresh')  # time at next scr refresh
                # update status
                maxPain.status = STARTED
                maxPain.setAutoDraw(True)
            
            # if maxPain is active this frame...
            if maxPain.status == STARTED:
                # update params
                pass
            
            # *red_int* updates
            
            # if red_int is starting this frame...
            if red_int.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_int.frameNStart = frameN  # exact frame index
                red_int.tStart = t  # local t and not account for scr refresh
                red_int.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_int, 'tStartRefresh')  # time at next scr refresh
                # update status
                red_int.status = STARTED
                red_int.setAutoDraw(True)
            
            # if red_int is active this frame...
            if red_int.status == STARTED:
                # update params
                pass
            
            # *white_int* updates
            
            # if white_int is starting this frame...
            if white_int.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                white_int.frameNStart = frameN  # exact frame index
                white_int.tStart = t  # local t and not account for scr refresh
                white_int.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(white_int, 'tStartRefresh')  # time at next scr refresh
                # update status
                white_int.status = STARTED
                white_int.setAutoDraw(True)
            
            # if white_int is active this frame...
            if white_int.status == STARTED:
                # update params
                white_int.setPos((intX,0), log=False)
            
            # *leftTr* updates
            
            # if leftTr is starting this frame...
            if leftTr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftTr.frameNStart = frameN  # exact frame index
                leftTr.tStart = t  # local t and not account for scr refresh
                leftTr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftTr, 'tStartRefresh')  # time at next scr refresh
                # update status
                leftTr.status = STARTED
                leftTr.setAutoDraw(True)
            
            # if leftTr is active this frame...
            if leftTr.status == STARTED:
                # update params
                pass
            
            # *rightTri* updates
            
            # if rightTri is starting this frame...
            if rightTri.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightTri.frameNStart = frameN  # exact frame index
                rightTri.tStart = t  # local t and not account for scr refresh
                rightTri.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightTri, 'tStartRefresh')  # time at next scr refresh
                # update status
                rightTri.status = STARTED
                rightTri.setAutoDraw(True)
            
            # if rightTri is active this frame...
            if rightTri.status == STARTED:
                # update params
                pass
            # *MouseInt* updates
            
            # if MouseInt is starting this frame...
            if MouseInt.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MouseInt.frameNStart = frameN  # exact frame index
                MouseInt.tStart = t  # local t and not account for scr refresh
                MouseInt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MouseInt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('MouseInt.started', t)
                # update status
                MouseInt.status = STARTED
                MouseInt.mouseClock.reset()
                prevButtonState = MouseInt.getPressed()  # if button is down already this ISN'T a new click
            if MouseInt.status == STARTED:  # only update if started and not finished!
                buttons = MouseInt.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # end routine on response            # Run 'Each Frame' code from IntCode
            #white_rect.setPos((mouse.getPos()[0],0), log=False)
            win.mouseVisible = False
            currentPosI = MouseInt.getPos()
            xPosI = currentPosI[0]
            #xPos = [mouse.getPos()[0], 0]
            if xPosI < -7.5:
                intX=-7.5
            elif xPosI > 7.5:
            #    whitePos=(8.375,0)
                intX=7.5
            else:
            #    whitePos=(xPos,0)
                intX=xPosI
            
            # *intensInstruction* updates
            
            # if intensInstruction is starting this frame...
            if intensInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intensInstruction.frameNStart = frameN  # exact frame index
                intensInstruction.tStart = t  # local t and not account for scr refresh
                intensInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intensInstruction, 'tStartRefresh')  # time at next scr refresh
                # update status
                intensInstruction.status = STARTED
                intensInstruction.setAutoDraw(True)
            
            # if intensInstruction is active this frame...
            if intensInstruction.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PAIN_intComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PAIN_int" ---
        for thisComponent in PAIN_intComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('PAIN_int.stopped', globalClock.getTime())
        # store data for loopSize (TrialHandler)
        x, y = MouseInt.getPos()
        buttons = MouseInt.getPressed()
        loopSize.addData('MouseInt.x', x)
        loopSize.addData('MouseInt.y', y)
        loopSize.addData('MouseInt.leftButton', buttons[0])
        loopSize.addData('MouseInt.midButton', buttons[1])
        loopSize.addData('MouseInt.rightButton', buttons[2])
        # Run 'End Routine' code from IntCode
        mouse_click = MouseInt.getPos()
        x_clickI = mouse_click[0]
        #xPos = [mouse.getPos()[0], 0]
        if x_clickI < -7.5:
            intX_click=-7.5
        
        elif x_clickI > 7.5:
        #    whitePos=(8.375,0)
            intX_click=7.5
        
        else:
        #    whitePos=(xPos,0)
            intX_click=xPosI
        #white_rect.setPos((xPos,0), log=False)
        distance = round((intX_click - (-7.5))*(0.66666666667),3)
        
        loopSize.addData('Intensity_Rating', distance)
        loopSize.addData('Intensity_Rating_duration(sec)', t)
        # the Routine "PAIN_int" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "PAIN_unp" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('PAIN_unp.started', globalClock.getTime())
        # setup some python lists for storing info about the MouseUnp
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from UnpCode
        #Mouse settings
        intX=-7.5
        MouseUnp.setPos((-7.5,0))
        
        #Task
        rateUnp = visual.TextStim(win,unp_PainTask,
        color='white', colorSpace='rgb', alignText='center',units='cm', pos=(0,9), height=1.3, wrapWidth=35)
        
        #Left anchor of VAS
        noUnp = visual.TextStim(win, unp_PainLeft, color='white', colorSpace='rgb',
        alignText='center', units='cm', pos=(-16,3), height=0.5)
        
        #Right anchor of VAS
        maxUnp = visual.TextStim(win, unp_PainRight, color='white', colorSpace='rgb',
        alignText='center', units='cm', pos=(2,3), height=0.5)
        
        #VAS instruction
        unpInstruction = visual.TextStim(win, unp_PainInstr,
                               color='white', colorSpace='rgb', alignText='center',units='cm', pos=(0,-9), height=0.6, wrapWidth=30)
        
        # keep track of which components have finished
        PAIN_unpComponents = [rateUnp, noUnp, maxUnp, red_Unp, white_Unp, leftAr, rightAr, MouseUnp, unpInstruction]
        for thisComponent in PAIN_unpComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PAIN_unp" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rateUnp* updates
            
            # if rateUnp is starting this frame...
            if rateUnp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rateUnp.frameNStart = frameN  # exact frame index
                rateUnp.tStart = t  # local t and not account for scr refresh
                rateUnp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rateUnp, 'tStartRefresh')  # time at next scr refresh
                # update status
                rateUnp.status = STARTED
                rateUnp.setAutoDraw(True)
            
            # if rateUnp is active this frame...
            if rateUnp.status == STARTED:
                # update params
                pass
            
            # *noUnp* updates
            
            # if noUnp is starting this frame...
            if noUnp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                noUnp.frameNStart = frameN  # exact frame index
                noUnp.tStart = t  # local t and not account for scr refresh
                noUnp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noUnp, 'tStartRefresh')  # time at next scr refresh
                # update status
                noUnp.status = STARTED
                noUnp.setAutoDraw(True)
            
            # if noUnp is active this frame...
            if noUnp.status == STARTED:
                # update params
                pass
            
            # *maxUnp* updates
            
            # if maxUnp is starting this frame...
            if maxUnp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                maxUnp.frameNStart = frameN  # exact frame index
                maxUnp.tStart = t  # local t and not account for scr refresh
                maxUnp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(maxUnp, 'tStartRefresh')  # time at next scr refresh
                # update status
                maxUnp.status = STARTED
                maxUnp.setAutoDraw(True)
            
            # if maxUnp is active this frame...
            if maxUnp.status == STARTED:
                # update params
                pass
            
            # *red_Unp* updates
            
            # if red_Unp is starting this frame...
            if red_Unp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_Unp.frameNStart = frameN  # exact frame index
                red_Unp.tStart = t  # local t and not account for scr refresh
                red_Unp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_Unp, 'tStartRefresh')  # time at next scr refresh
                # update status
                red_Unp.status = STARTED
                red_Unp.setAutoDraw(True)
            
            # if red_Unp is active this frame...
            if red_Unp.status == STARTED:
                # update params
                pass
            
            # *white_Unp* updates
            
            # if white_Unp is starting this frame...
            if white_Unp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                white_Unp.frameNStart = frameN  # exact frame index
                white_Unp.tStart = t  # local t and not account for scr refresh
                white_Unp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(white_Unp, 'tStartRefresh')  # time at next scr refresh
                # update status
                white_Unp.status = STARTED
                white_Unp.setAutoDraw(True)
            
            # if white_Unp is active this frame...
            if white_Unp.status == STARTED:
                # update params
                white_Unp.setPos((intX,0), log=False)
            
            # *leftAr* updates
            
            # if leftAr is starting this frame...
            if leftAr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftAr.frameNStart = frameN  # exact frame index
                leftAr.tStart = t  # local t and not account for scr refresh
                leftAr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftAr, 'tStartRefresh')  # time at next scr refresh
                # update status
                leftAr.status = STARTED
                leftAr.setAutoDraw(True)
            
            # if leftAr is active this frame...
            if leftAr.status == STARTED:
                # update params
                pass
            
            # *rightAr* updates
            
            # if rightAr is starting this frame...
            if rightAr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightAr.frameNStart = frameN  # exact frame index
                rightAr.tStart = t  # local t and not account for scr refresh
                rightAr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightAr, 'tStartRefresh')  # time at next scr refresh
                # update status
                rightAr.status = STARTED
                rightAr.setAutoDraw(True)
            
            # if rightAr is active this frame...
            if rightAr.status == STARTED:
                # update params
                pass
            # *MouseUnp* updates
            
            # if MouseUnp is starting this frame...
            if MouseUnp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MouseUnp.frameNStart = frameN  # exact frame index
                MouseUnp.tStart = t  # local t and not account for scr refresh
                MouseUnp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MouseUnp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('MouseUnp.started', t)
                # update status
                MouseUnp.status = STARTED
                MouseUnp.mouseClock.reset()
                prevButtonState = MouseUnp.getPressed()  # if button is down already this ISN'T a new click
            if MouseUnp.status == STARTED:  # only update if started and not finished!
                buttons = MouseUnp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # end routine on response            # Run 'Each Frame' code from UnpCode
            #white_rect.setPos((mouse.getPos()[0],0), log=False)
            win.mouseVisible = False
            currentPosI = MouseUnp.getPos()
            xPosI = currentPosI[0]
            #xPos = [mouse.getPos()[0], 0]
            if xPosI < -7.5:
                intX=-7.5
            elif xPosI > 7.5:
            #    whitePos=(8.375,0)
                intX=7.5
            else:
            #    whitePos=(xPos,0)
                intX=xPosI
            
            
            # *unpInstruction* updates
            
            # if unpInstruction is starting this frame...
            if unpInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                unpInstruction.frameNStart = frameN  # exact frame index
                unpInstruction.tStart = t  # local t and not account for scr refresh
                unpInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(unpInstruction, 'tStartRefresh')  # time at next scr refresh
                # update status
                unpInstruction.status = STARTED
                unpInstruction.setAutoDraw(True)
            
            # if unpInstruction is active this frame...
            if unpInstruction.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PAIN_unpComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PAIN_unp" ---
        for thisComponent in PAIN_unpComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('PAIN_unp.stopped', globalClock.getTime())
        # store data for loopSize (TrialHandler)
        x, y = MouseUnp.getPos()
        buttons = MouseUnp.getPressed()
        loopSize.addData('MouseUnp.x', x)
        loopSize.addData('MouseUnp.y', y)
        loopSize.addData('MouseUnp.leftButton', buttons[0])
        loopSize.addData('MouseUnp.midButton', buttons[1])
        loopSize.addData('MouseUnp.rightButton', buttons[2])
        # Run 'End Routine' code from UnpCode
        mouse_click = MouseUnp.getPos()
        x_clickI = mouse_click[0]
        #xPos = [mouse.getPos()[0], 0]
        if x_clickI < -7.5:
            intX_click=-7.5
        
        elif x_clickI > 7.5:
        #    whitePos=(8.375,0)
            intX_click=7.5
        
        else:
        #    whitePos=(xPos,0)
            intX_click=xPosI
        #white_rect.setPos((xPos,0), log=False)
        distance = round((intX_click - (-7.5))*(0.66666666667),3)
        
        loopSize.addData('Unpleasant_Rating', distance)
        loopSize.addData('Unpleasant_Rating_duration(sec)', t)
        # the Routine "PAIN_unp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'loopSize'
    
    # get names of stimulus parameters
    if loopSize.trialList in ([], [None], None):
        params = []
    else:
        params = loopSize.trialList[0].keys()
    # save data for this loop
    loopSize.saveAsExcel(filename + '.xlsx', sheetName='loopSize',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    loopSize.saveAsText(filename + 'loopSize.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "Closing" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Closing.started', globalClock.getTime())
    keyEnding.keys = []
    keyEnding.rt = []
    _keyEnding_allKeys = []
    # Run 'Begin Routine' code from codeEnding
    from painSize_instructions_20240425 import ending
    textEnd = visual.TextStim(win, ending,
                           color=(255,255,255), colorSpace='rgb', alignText='center',units='cm', pos=(0,0), height=0.8, wrapWidth=30)
    # keep track of which components have finished
    ClosingComponents = [textEnd, keyEnding]
    for thisComponent in ClosingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Closing" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textEnd* updates
        
        # if textEnd is starting this frame...
        if textEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textEnd.frameNStart = frameN  # exact frame index
            textEnd.tStart = t  # local t and not account for scr refresh
            textEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textEnd, 'tStartRefresh')  # time at next scr refresh
            # update status
            textEnd.status = STARTED
            textEnd.setAutoDraw(True)
        
        # if textEnd is active this frame...
        if textEnd.status == STARTED:
            # update params
            pass
        
        # *keyEnding* updates
        waitOnFlip = False
        
        # if keyEnding is starting this frame...
        if keyEnding.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyEnding.frameNStart = frameN  # exact frame index
            keyEnding.tStart = t  # local t and not account for scr refresh
            keyEnding.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyEnding, 'tStartRefresh')  # time at next scr refresh
            # update status
            keyEnding.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyEnding.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyEnding.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyEnding.status == STARTED and not waitOnFlip:
            theseKeys = keyEnding.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyEnding_allKeys.extend(theseKeys)
            if len(_keyEnding_allKeys):
                keyEnding.keys = _keyEnding_allKeys[-1].name  # just the last key pressed
                keyEnding.rt = _keyEnding_allKeys[-1].rt
                keyEnding.duration = _keyEnding_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ClosingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Closing" ---
    for thisComponent in ClosingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Closing.stopped', globalClock.getTime())
    # check responses
    if keyEnding.keys in ['', [], None]:  # No response was made
        keyEnding.keys = None
    thisExp.addData('keyEnding.keys',keyEnding.keys)
    if keyEnding.keys != None:  # we had a response
        thisExp.addData('keyEnding.rt', keyEnding.rt)
        thisExp.addData('keyEnding.duration', keyEnding.duration)
    thisExp.nextEntry()
    # the Routine "Closing" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
