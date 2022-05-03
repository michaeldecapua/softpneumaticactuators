# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

#Load variables
#execfile('Vara.py')
state1 = 50.0
state2 = 20.0
state3 = 10.0
state4 = 2.0

La = state1
H = state2
Lc = state3
T = state4
Hc = 5
Lk = (La- 3*Lc)/2

pressure = 0.01
force = 0.8621

s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints

s1.setPrimaryObject(option=STANDALONE)

    
#Changeable code
# outer sketch ------------------------------------------------------
s1.Line(point1=(0.0, 0.0), point2=(La, 0.0))
s1.HorizontalConstraint(entity=g[2], addUndoState=False)
# s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-21.2945175170898,
#    -20.1835823059082), value=state1)
s1.Line(point1=(0.0, 0.0), point2=(0.0, H))
s1.VerticalConstraint(entity=g[3], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s1.Line(point1=(0.0, H), point2=(Lc, H))
s1.HorizontalConstraint(entity=g[4], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s1.Line(point1=(Lc, H), point2=(Lc, Hc))
s1.VerticalConstraint(entity=g[5], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s1.Line(point1=(Lc, Hc), point2=(Lc + Lk, Hc))
s1.HorizontalConstraint(entity=g[6], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s1.Line(point1=(Lc + Lk, Hc), point2=(Lc + Lk, H))
s1.VerticalConstraint(entity=g[7], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s1.Line(point1=(Lc + Lk, H), point2=(2 * Lc + Lk, H))
s1.HorizontalConstraint(entity=g[8], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
s1.Line(point1=(2 * Lc + Lk, H), point2=(2 * Lc + Lk, Hc))
s1.VerticalConstraint(entity=g[9], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s1.Line(point1=(2 * Lc + Lk, Hc), point2=(2 * Lc + 2 * Lk, Hc))
s1.HorizontalConstraint(entity=g[10], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
s1.Line(point1=(2 * Lc + 2 * Lk, Hc), point2=(2 * Lc + 2 * Lk, H))
s1.VerticalConstraint(entity=g[11], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
s1.Line(point1=(2 * Lc + 2 * Lk, H), point2=(La, H))
s1.HorizontalConstraint(entity=g[12], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
s1.Line(point1=(La, H), point2=(La, 0))
s1.VerticalConstraint(entity=g[13], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
# s.ObliqueDimension(vertex1=v[0], vertex2=v[2], textPoint=(-41.9849395751953,
#   0.226783752441406), value=state2)
# s.ObliqueDimension(vertex1=v[11], vertex2=v[1], textPoint=(29.4498672485352,
#    -2.64579010009766), value=state2)
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D,
                               type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseSolidExtrude(sketch=s1, depth=20.0)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Part-1']
p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=4.0)
p = mdb.models['Model-1'].parts['Part-1']
e, d1 = p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=d1[2], sketchUpEdge=e[30],
                          sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0, 0.0,
                                                                                  4.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                             sheetSize=134.82, gridSpacing=3.37, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)

#-------------------------------------------------------------------------
# inner sketch----------------------------------------------------------
s1.Line(point1=(0.0+T, 0.0+T), point2=(La-T, 0.0+T))
s1.HorizontalConstraint(entity=g[2], addUndoState=False)
# s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-21.2945175170898,
#    -20.1835823059082), value=state1)
s1.Line(point1=(0.0+T, 0.0+T), point2=(0.0+T, H-T))
s1.VerticalConstraint(entity=g[3], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s1.Line(point1=(0.0+T, H-T), point2=(Lc-T, H-T))
s1.HorizontalConstraint(entity=g[4], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s1.Line(point1=(Lc-T, H-T), point2=(Lc-T, Hc-T))
s1.VerticalConstraint(entity=g[5], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s1.Line(point1=(Lc-T, Hc-T), point2=(Lc + Lk+T, Hc-T))
s1.HorizontalConstraint(entity=g[6], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s1.Line(point1=(Lc + Lk+T, Hc-T), point2=(Lc + Lk+T, H-T))
s1.VerticalConstraint(entity=g[7], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s1.Line(point1=(Lc + Lk+T, H-T), point2=(2 * Lc + Lk-T, H-T))
s1.HorizontalConstraint(entity=g[8], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
s1.Line(point1=(2 * Lc + Lk-T, H-T), point2=(2 * Lc + Lk-T, Hc-T))
s1.VerticalConstraint(entity=g[9], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s1.Line(point1=(2 * Lc + Lk-T, Hc-T), point2=(2 * Lc + 2 * Lk+T, Hc-T))
s1.HorizontalConstraint(entity=g[10], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
s1.Line(point1=(2 * Lc + 2 * Lk+T, Hc-T), point2=(2 * Lc + 2 * Lk+T, H-T))
s1.VerticalConstraint(entity=g[11], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
s1.Line(point1=(2 * Lc + 2 * Lk+T, H-T), point2=(La-T, H-T))
s1.HorizontalConstraint(entity=g[12], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
s1.Line(point1=(La-T, H-T), point2=(La-T, 0+T))
s1.VerticalConstraint(entity=g[13], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
# s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-19.7394065856934,
#    11.6468391418457), value=state3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=106.1,
                                                farPlane=163.545, width=134.024, height=58.4936, cameraPosition=(
        -15.1913, -4.30403, 144.822), cameraTarget=(-15.1913, -4.30403, 10))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-2.94987,
                                                                12.7513, 144.822), cameraTarget=(-2.94987, 12.7513, 10))
session.viewports['Viewport: 1'].view.setValues(nearPlane=111.082,
                                                farPlane=158.563, width=86.9117, height=37.9318, cameraPosition=(
        -6.91756, 14.7611, 144.822), cameraTarget=(-6.91756, 14.7611, 10))
# s1.ObliqueDimension(vertex1=v[4], vertex2=v[5], textPoint=(0.255085468292236,
#    14.8020210266113), value=state3)
# s1.ObliqueDimension(vertex1=v[8], vertex2=v[9], textPoint=(21.7784233093262,
#    15.7851333618164), value=state3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=109.144,
                                                farPlane=160.5, width=99.1674, height=43.2806, cameraPosition=(
        -18.0875, 10.0777, 144.822), cameraTarget=(-18.0875, 10.0777, 10))
# s1.ObliqueDimension(vertex1=v[11], vertex2=v[0], textPoint=(-35.8929290771484,
#    -1.27991199493408), value=state4)
# s1.ObliqueDimension(vertex1=v[9], vertex2=v[10], textPoint=(32.8332366943359,
#    0.309226036071777), value=state4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=102.096,
                                                farPlane=167.548, width=143.748, height=62.7374, cameraPosition=(
        -10.6119, 17.1345, 144.822), cameraTarget=(-10.6119, 17.1345, 10))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-7.63412,
                                                                0.603218, 144.822),
                                                cameraTarget=(-7.63412, 0.603218, 10))
session.viewports['Viewport: 1'].view.setValues(nearPlane=109.144,
                                                farPlane=160.5, width=99.1674, height=43.2806, cameraPosition=(
        -9.40268, 3.09716, 144.822), cameraTarget=(-9.40268, 3.09716, 10))
p = mdb.models['Model-1'].parts['Part-1']
e1, d2 = p.edges, p.datums
p.CutExtrude(sketchPlane=d2[2], sketchUpEdge=e1[30], sketchPlaneSide=SIDE1,
             sketchOrientation=RIGHT, sketch=s1, depth=12.0,
             flipExtrudeDirection=ON)
s1.unsetPrimaryObject()          #----------------------------cut extrude
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Density(table=((1.049e-09, ), ))
mdb.models['Model-1'].materials['Material-1'].Hyperelastic(materialType=
    ISOTROPIC, table=((0.11, 0.02, 0.0, 0.0, 0.0, 0.0), ), testData=OFF, type=
    YEOH, volumetricResponse=VOLUMETRIC_DATA)
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-1', name=
    'Section-1', thickness=None)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask((
    '[#1 ]', ), ), name='Set-1')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName=
    'Section-1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Surface(name='innerwalls', 
    side1Faces=
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask((
    '[#fffc0000 #f ]', ), ))
mdb.models['Model-1'].parts['Part-1'].Surface(name='outerwalls', 
    side1Faces=
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask((
    '[#aaa ]', ), ))
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1', 
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].StaticStep(initialInc=0.001, name='press', nlgeom=ON, 
    previous='Initial')
mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
    formulation=FRICTIONLESS)
mdb.models['Model-1'].SelfContactStd(createStepName='press', 
    interactionProperty='IntProp-1', name='Int-1', surface=
    mdb.models['Model-1'].rootAssembly.instances['Part-1'].surfaces['outerwalls']
    , thickness=ON)
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1'].faces.getSequenceFromMask(
    ('[#8000 ]', ), ), name='Set-1')
mdb.models['Model-1'].EncastreBC(createStepName='Initial', localCsys=None, 
    name='BC-1', region=mdb.models['Model-1'].rootAssembly.sets['Set-1'])
mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName='press', 
    distributionType=UNIFORM, field='', magnitude=0.01, name='press', region=
    mdb.models['Model-1'].rootAssembly.instances['Part-1'].surfaces['innerwalls'])
mdb.models['Model-1'].parts['Part-1'].setMeshControls(elemShape=TET, 
    regions=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask((
    '[#1 ]', ), ), technique=FREE)
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, 
    elemLibrary=STANDARD), ElemType(elemCode=C3D10, elemLibrary=STANDARD)), 
    regions=(
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask((
    '[#1 ]', ), ), ))
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=2.0)
mdb.models['Model-1'].parts['Part-1'].generateMesh()
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, 
    elemLibrary=STANDARD), ElemType(elemCode=C3D10H, elemLibrary=STANDARD)), 
    regions=(
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask((
    '[#1 ]', ), ), ))
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='final_pneunet', nodalOutputPrecision=
    SINGLE, numCpus=3, numDomains=3, numGPUs=0, queue=None, resultsFormat=ODB, 
    scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)

mdb.jobs['final_pneunet'].submit(consistencyChecking=ON)
  
mdb.jobs['final_pneunet'].waitForCompletion()  
session.mdbData.summary()
    
o3 = session.openOdb(
name=r"C:\Users\ronn\OneDrive\Desktop\Optimize finger\testrun2\tforce.odb")
    
session.viewports['Viewport: 1'].setValues(displayedObject=o3)  
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
    
odb = session.odbs[r'C:\Users\ronn\OneDrive\Desktop\Optimize finger\testrun2\tforce.odb']
    
session.writeFieldReport(fileName='abaqus_results.rpt',append=OFF,sortItem='Node Label',odb=odb,step=0,frame=1,outputPosition=NODAL,variable=(('U', NODAL,((COMPONENT,'U1'),(COMPONENT,'U2'), (
COMPONENT,'U3'),)),))
    
mdb.saveAs(
pathName=r'C:\Users\ronn\OneDrive\Desktop\Optimize finger\testrun2\tforce')

# Save by ronn on 2022_04_29-12.29.29; build 2021 2020_03_06-07.50.37 167380
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.jobs['final_pneunet'].submit(consistencyChecking=OFF)
mdb.jobs['final_pneunet']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'LAPTOP-J2494IUA', 'handle': 0, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\temp\\final_pneunet.odb', 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'LAPTOP-J2494IUA', 'handle': 36096, 
    'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 0, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'final_pneunet', 'memory': 845.0})
mdb.jobs['final_pneunet']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16150.0, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(MINIMUM_MEMORY, {'minimum_memory': 140.0, 
    'phase': STANDARD_PHASE, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.001, 'attempts': 1, 
    'timeIncrement': 0.001, 'increment': 1, 'stepTime': 0.001, 'step': 1, 
    'jobName': 'final_pneunet', 'severe': 0, 'iterations': 2, 
    'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 1, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.002, 'attempts': 1, 
    'timeIncrement': 0.001, 'increment': 2, 'stepTime': 0.002, 'step': 1, 
    'jobName': 'final_pneunet', 'severe': 0, 'iterations': 1, 
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 2, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.0035, 'attempts': 1, 
    'timeIncrement': 0.0015, 'increment': 3, 'stepTime': 0.0035, 'step': 1, 
    'jobName': 'final_pneunet', 'severe': 0, 'iterations': 1, 
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 3, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.00575, 
    'attempts': 1, 'timeIncrement': 0.00225, 'increment': 4, 
    'stepTime': 0.00575, 'step': 1, 'jobName': 'final_pneunet', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 4, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.009125, 
    'attempts': 1, 'timeIncrement': 0.003375, 'increment': 5, 
    'stepTime': 0.009125, 'step': 1, 'jobName': 'final_pneunet', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 5, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.0141875, 
    'attempts': 1, 'timeIncrement': 0.0050625, 'increment': 6, 
    'stepTime': 0.0141875, 'step': 1, 'jobName': 'final_pneunet', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 6, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.02178125, 
    'attempts': 1, 'timeIncrement': 0.00759375, 'increment': 7, 
    'stepTime': 0.02178125, 'step': 1, 'jobName': 'final_pneunet', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 7, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.033171875, 
    'attempts': 1, 'timeIncrement': 0.011390625, 'increment': 8, 
    'stepTime': 0.033171875, 'step': 1, 'jobName': 'final_pneunet', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 8, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.0502578125, 
    'attempts': 1, 'timeIncrement': 0.0170859375, 'increment': 9, 
    'stepTime': 0.0502578125, 'step': 1, 'jobName': 'final_pneunet', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 9, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.07588671875, 
    'attempts': 1, 'timeIncrement': 0.02562890625, 'increment': 10, 
    'stepTime': 0.07588671875, 'step': 1, 'jobName': 'final_pneunet', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 10, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.114330078125, 
    'attempts': 1, 'timeIncrement': 0.038443359375, 'increment': 11, 
    'stepTime': 0.114330078125, 'step': 1, 'jobName': 'final_pneunet', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 11, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.1719951171875, 
    'attempts': 1, 'timeIncrement': 0.0576650390625, 'increment': 12, 
    'stepTime': 0.1719951171875, 'step': 1, 'jobName': 'final_pneunet', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 12, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.25849267578125, 
    'attempts': 1, 'timeIncrement': 0.08649755859375, 'increment': 13, 
    'stepTime': 0.25849267578125, 'step': 1, 'jobName': 'final_pneunet', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 13, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.388239013671875, 
    'attempts': 1, 'timeIncrement': 0.129746337890625, 'increment': 14, 
    'stepTime': 0.388239013671875, 'step': 1, 'jobName': 'final_pneunet', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 14, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.582858520507813, 
    'attempts': 1, 'timeIncrement': 0.194619506835938, 'increment': 15, 
    'stepTime': 0.582858520507813, 'step': 1, 'jobName': 'final_pneunet', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 15, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 0.874787780761719, 
    'attempts': 1, 'timeIncrement': 0.291929260253906, 'increment': 16, 
    'stepTime': 0.874787780761719, 'step': 1, 'jobName': 'final_pneunet', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 16, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 17, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1, 
    'timeIncrement': 0.125212219238281, 'increment': 17, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'final_pneunet', 'severe': 0, 'iterations': 1, 
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['final_pneunet']._Message(END_STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'final_pneunet'})
mdb.jobs['final_pneunet']._Message(JOB_COMPLETED, {
    'time': 'Fri Apr 29 12:31:49 2022', 'jobName': 'final_pneunet'})
# Save by ronn on 2022_04_29-12.38.53; build 2021 2020_03_06-07.50.37 167380
